from db import vectordb

def search_title(query, top_k=3):
    exact_title_results = vectordb.get(where={"title": query})

    if exact_title_results["documents"]:
        exact_title = query
        exact_text = vectordb.similarity_search(exact_title, k=1)

        title_results = vectordb.similarity_search(query, k=top_k + 3)
        similar_titles = list(set([res.metadata.get("title", "") for res in title_results if res.metadata.get("title", "") != exact_title]))[:2]

        extra_texts = []
        for t in similar_titles:
            t_results = vectordb.similarity_search(t, k=1)
            extra_texts.extend(t_results)

        return exact_text + extra_texts

    title_results = vectordb.similarity_search(query, k=top_k * 2)
    similar_titles = list(set([res.metadata.get("title", "") for res in title_results]))[:top_k]

    all_texts = []
    for t in similar_titles:
        t_results = vectordb.similarity_search(t, k=1)
        all_texts.extend(t_results)

    return all_texts
