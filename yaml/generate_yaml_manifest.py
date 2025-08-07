from jinja2 import Environment, FileSystemLoader
import os

CLUSTER = os.environ['CLUSTER']
NAMESPACE = os.environ['NAMESPACE']
MILVUS_IMAGE_VERSION = os.environ['MILVUS_IMAGE_VERSION']
BUCKET_NAME = os.environ['BUCKET_NAME']
ATTU_IMAGE_VERSION = os.environ['ATTU_IMAGE_VERSION']
SORT_NAMESPACE = "-".join(NAMESPACE.split("-")[-2:])
print(CLUSTER)
print(NAMESPACE)
print(MILVUS_IMAGE_VERSION)
print(BUCKET_NAME)
print(ATTU_IMAGE_VERSION)
print(SORT_NAMESPACE)
if CLUSTER == 'dev':
    SORT_CLUSTER = 'brown'
else:
    SORT_CLUSTER = CLUSTER

env = Environment(loader=FileSystemLoader("./templates"))
templates = env.get_template("yaml_template.yaml.j2")
content = templates.render(
    cluster = CLUSTER,  
    namespace = NAMESPACE,
    milvus_image_version =  MILVUS_IMAGE_VERSION,
    bucket_name = BUCKET_NAME,
    attu_image_version = ATTU_IMAGE_VERSION,
    sort_namespace = SORT_NAMESPACE,
    sort_cluster = SORT_CLUSTER
)

filename = f"./{CLUSTER}/{NAMESPACE}.yaml"

with open(filename,'w') as f:
    f.write(content)
    print(f"milvus manifest file {filename} created.")