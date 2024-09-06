from elasticsearch import Elasticsearch

# Credenciais de autenticação
username = 'elastic'
password = '0cVw0WXaXDns3sq3V06'

# Conectando ao cluster Elasticsearch
es = Elasticsearch(
    hosts=[{
        'host': 'localhost',
        'port': 9200,
        'scheme': 'http'  # ou 'https' se estiver usando SSL
    }],
    basic_auth=(username, password)
)

# Nome do índice que você quer consultar
index_name = 'amazon_azure_finops'

# Query personalizada (exemplo de busca por uma string em um campo específico)
search_query = {
    "size": 0,
    "aggs": {
        "average_cloud_cost": {
            "avg": {
                "field": "cost"
            }
        }
    }
}

# Buscando dados no índice
response = es.search(index=index_name, body=search_query)
# Extraindo o valor da agregação "average_cloud_cost"
average_cloud_cost = response['aggregations']['average_cloud_cost']['value']

# Exibindo o resultado
print(f"Average Cloud Cost: {average_cloud_cost}")

# # Exibindo os resultados
# for hit in response['hits']['hits']:
#     print(hit['_source'])

# # Buscando com paginação
# page_size = 10
# page_number = 1

# paginated_response = es.search(
#     index=index_name,
#     body=search_query,
#     from_=(page_number - 1) * page_size,
#     size=page_size
# )

# print(f"Resultados página {page_number}:")
# for hit in paginated_response['hits']['hits']:
#     print(hit['_source'])
