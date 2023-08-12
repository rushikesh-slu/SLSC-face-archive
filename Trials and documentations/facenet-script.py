import os
import csv
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from torchvision.transforms import ToTensor
from facenet_pytorch import MTCNN, InceptionResnetV1
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
import ssl
import uuid

ssl._create_default_https_context = ssl._create_unverified_context

# Function to load an image from file and preprocess it
def load_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img = transform(img)
    return img

# Function to get face embeddings from an image
def get_face_embedding(img, resnet):
    return resnet(img.unsqueeze(0)).detach().numpy()[0]

# Replace 'path_to_image_folder' with the path to your image folder
image_folder = '/Users/beffiong/desktop/YES JPEGs'
output_csv = 'output.csv'

# Initialize MTCNN and InceptionResnetV1
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
mtcnn = MTCNN(keep_all=True, device=device)
resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

# List all the image files in the folder
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith('.jpg')]

# Create a list to store face embeddings and image paths
embeddings = []
image_paths = []

# Define the image transformation for the InceptionResnetV1 model
transform = transforms.Compose([
    transforms.Resize(160),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Create a dictionary to store UUIDs as keys and a list of image names as values
uuid_dict = {}

# Process each image and extract face embeddings
for image_path in image_files:
    try:
        img = load_image(image_path).to(device)
        face_embedding = get_face_embedding(img, resnet)
        embeddings.append(face_embedding)
        image_paths.append(image_path)

        # Get the person's name (replace this with your logic to get the person's name from the image path)
        person_name = os.path.basename(image_path).split('.')[0]

        # Check if the person's UUID already exists in the dictionary
        if person_name in uuid_dict:
            # If it exists, add the image name to the existing UUID's list of images
            uuid_dict[person_name].append(os.path.basename(image_path))
        else:
            # If it doesn't exist, generate a new UUID and create a new entry in the dictionary
            new_uuid = str(uuid.uuid4())
            uuid_dict[person_name] = [os.path.basename(image_path)]
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

# Save the face embeddings and image paths with cluster numbers to a CSV file
with open(output_csv, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['UUID', 'Cluster', 'Image_Names'])

    # Perform clustering using DBSCAN
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    cluster_labels = dbscan.fit_predict(embeddings)

    # Determine the number of clusters (excluding noise points)
    num_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)

    # Create a dictionary to store UUIDs as keys and a list of image names and cluster numbers as values
    uuid_dict_with_cluster = {}

    # Update the dictionary with the cluster number for each person and their images
    for person_name, image_list in uuid_dict.items():
        cluster_number = cluster_labels[image_paths.index(os.path.join(image_folder, image_list[0]))]
        uuid_dict_with_cluster[person_name] = {'cluster': cluster_number, 'images': image_list}

    # Write the data to the CSV file
    for person_name, cluster_info in uuid_dict_with_cluster.items():
        cluster_number = cluster_info['cluster']
        image_list = cluster_info['images']
        csv_writer.writerow([person_name, cluster_number, ', '.join(image_list)])

# Apply t-SNE to reduce the embeddings to 2D
# Convert embeddings from a list of 1D arrays to a 2D array
embeddings_2d_array = np.array(embeddings)

# Apply t-SNE to reduce the embeddings to 2D
tsne = TSNE(n_components=2, random_state=0)
embeddings_2d = tsne.fit_transform(embeddings_2d_array)

# Create a scatter plot of the 2D embeddings with clustering and circles
plt.figure(figsize=(8, 6))

# Plot each point with a different color based on its cluster
for i in range(num_clusters):
    cluster_points = embeddings_2d[cluster_labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], marker='o', label=f'Cluster {i}')

plt.title('t-SNE Visualization with DBSCAN Clustering')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.legend()
plt.show()