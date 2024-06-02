import csv
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_embedding(text, model="model-identifier"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def process_csv(input_file, output_file, model="model-identifier"):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Manually set the header
        header = ["agent_name", "message"]
        
        # Get the first embedding to determine its size
        first_row = next(reader)
        agent_name, message = first_row
        first_embedding = get_embedding(message, model)
        embedding_size = len(first_embedding)
        
        # Write the new header to the output file
        writer.writerow(header + ["embedding_" + str(i) for i in range(embedding_size)])
        
        # Write the first row with its embedding
        writer.writerow(first_row + first_embedding)
        
        # Process the remaining rows
        for row in reader:
            agent_name, message = row
            embedding = get_embedding(message, model)
            writer.writerow(row + embedding)

if __name__ == "__main__":
    input_file = 'agent_responses.csv'
    output_file = 'agent_responses_embeddings.csv'
    model = "nomic-ai/nomic-embed-text-v1.5-GGUF"  # Replace with your actual model identifier
    process_csv(input_file, output_file, model)