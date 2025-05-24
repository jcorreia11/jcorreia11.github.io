from scholarly import scholarly
import json


def get_scholar_citations():
    """
    Retrieves citation counts for papers listed in a JSON file using their DOIs.
    The JSON file should contain a mapping of paper titles to DOIs.
    The results are saved in a new JSON file with the DOI as the key and citation count as the value.
    """
    # read json file containing the DOIs
    file = 'papers.json'
    with open(file, 'r') as f:
        data = json.load(f)

    citations = []
    doi_to_citations = {}
    # Loop through each paper in the JSON data
    for paper, doi in data.items():
        try:
            query = scholarly.search_pubs(doi)
            result = next(query)
            doi_to_citations[doi] = result['num_citations']
        except Exception as e:
            print(f"Error retrieving data for DOI {doi}: {e}")
            doi_to_citations[doi] = None

    # save the results to a JSON file
    with open('../_data/citations_scholar.json', 'w') as f:
        json.dump(doi_to_citations, f, indent=4)

if __name__ == "__main__":
    get_scholar_citations()
    print("Citations have been retrieved and saved to 'citations_scholar.json'.")
