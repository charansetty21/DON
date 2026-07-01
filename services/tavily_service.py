import os

from dotenv import load_dotenv
from tavily import TavilyClient
from services.ollama_service import ask_llm

load_dotenv()

API_KEY = os.getenv("TAVILY_API_KEY")

if not API_KEY:
    raise ValueError("TAVILY_API_KEY not found in .env")

client = TavilyClient(api_key=API_KEY)


# =====================================================
# WEB SEARCH
# =====================================================

def search_web(query: str):
    """
    Perform an internet search using Tavily.
    """

    try:
        response = client.search(
            query=query,
            search_depth="advanced",
            topic="general",
            max_results=5,
            include_answer=True,
            include_raw_content=False,
        )

        return response

    except Exception as e:
        return {"error": str(e)}


# =====================================================
# FILTER RESULTS
# =====================================================

def filter_results(results):
    """
    Keep only useful search results.
    """

    filtered = []

    for item in results:
        title = item.get("title", "")
        content = item.get("content", "")

        if len(content.strip()) < 80:
            continue

        filtered.append(
            {
                "title": title,
                "content": content,
                "url": item.get("url", ""),
            }
        )

    return filtered[:3]


# =====================================================
# SEARCH + AI SUMMARY
# =====================================================

def search_and_summarize(query: str):
    """
    Search the web and summarize using Qwen.
    """

    result = search_web(query)

    if "error" in result:
        return f"Search Error: {result['error']}"

    results = filter_results(result.get("results", []))

    if not results:
        return "Boss, I couldn't find useful search results."

    context = ""
    sources = []

    for i, item in enumerate(results, start=1):

        title = item["title"]
        content = item["content"]
        url = item["url"]

        sources.append(url)

        context += f"""
Search Result {i}

Title:
{title}

Content:
{content}

Source:
{url}

---------------------------------------
"""

    # DEBUG: Print search results
    print("\n" + "=" * 80)
    print("RAW SEARCH RESULTS")
    print("=" * 80)
    print(context)
    print("=" * 80 + "\n")

    prompt = f"""
You are DON, an intelligent AI assistant.

You MUST answer ONLY using the search results below.

Rules:
1. Do NOT use your own knowledge.
2. Use ONLY the search results.
3. If multiple meanings exist, choose the one most strongly supported.
4. Never invent facts.
5. If the answer isn't in the search results, say so.
6. End with a short answer.

User Question:
{query}

Search Results:

{context}
"""

    answer = ask_llm(prompt)

    answer += "\n\nSources:\n"

    for url in sources:
        answer += f"- {url}\n"

    return answer