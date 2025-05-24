import warnings
import json
import pybliometrics
from pybliometrics.scopus import AbstractRetrieval


def get_scopus_citations():
    """
    Retrieves citation counts for papers listed in a JSON file using their DOIs.
    The JSON file should contain a mapping of paper titles to DOIs.
    The results are saved in a new JSON file with the DOI as the key and citation count as the value.
    """
    # General warning to remember to connect to UM VPN
    warnings.warn("Remember to connect to the UM VPN to access Scopus data.")

    pybliometrics.init()

    # read json file containing the DOIs
    file = 'papers.json'
    with open(file, 'r') as f:
        data = json.load(f)

    doi_to_citations = {}
    # Loop through each paper in the JSON data
    for paper, doi in data.items():
        try:
            # Retrieve the abstract using the DOI
            abstract = AbstractRetrieval(doi, view='FULL')
            # Extract the citation count
            citation_count = abstract.citedby_count
            # Store the citation count in the dictionary
            doi_to_citations[doi] = citation_count
        except Exception as e:
            print(f"Error retrieving data for DOI {doi}: {e}")
            doi_to_citations[doi] = None

    # save the results to a JSON file
    with open('../_data/citations_scopus.json', 'w') as f:
        json.dump(doi_to_citations, f, indent=4)

if __name__ == "__main__":
    get_scopus_citations()
    print("Citations have been retrieved and saved to 'citations_scopus.json'.")
