# LMAgents
Small demo for a bot group chat using LMStudio.


## Features

- Group chat with multiple AI agents.
- Agents respond based on predefined personalities and prompts.
- Real-time chat interface using Flask and Socket.IO.
- Save agent responses to a CSV file.
- Extract embeddings from agent responses.


## Getting Started

### Prerequisites

- LM Studio 
- Python 3.6+
- Flask
- Flask-SocketIO
- Flask-CORS
- OpenAI API

### Installation

1. Clone the repository:
```sh
git clone https://github.com/vschetinger/LMAgents.git
```
2. Create a virtual environment:
```sh
python -m venv LMAgents
```
3. Activate the virtual environment:
    - On **Windows**:
    ```sh
    LMAgents\Scripts\activate
    ```
    - On **macOS and Linux**:
    ```sh
    source LMAgents/bin/activate
    ```


4. Install the required dependencies:
```sh
pip install -r requirements.txt
```

5. Install LM Studio: https://lmstudio.ai/

6. Within LM Studio, download the models ```Llama 3 - 8B Instruct``` (essential, for  running the agents) and ```nomic embed text``` (any verison, for the embeddings)



### Usage

1. Open the "Local Server" tab on LM Studio, load ```Llama 3 - 8B Instruct``` and the embeddings, and start the servers.

2. Start the Flask application:
```sh
python app.py
```
3. Open your web browser and navigate to `http://127.0.0.1:5000`.

4. Enter a topic in the input field and click "Start Conversation" to begin the chat with the agents.


## Extracting embeddings

The `extract_embeddings.py` script allows you to extract embeddings from the agent responses and save them to a CSV file.

Run the script:
```sh
python extract_embeddings.py
```
The embeddings will be saved in `agent_responses_embeddings.csv`.

NOTE: the embeddings server must also have been started for this to work.

## Configuration

The agents are configured in the `agents_config.json` file. Each agent has the following properties:

- `name`: The name of the agent.
- `api_url`: The API URL for the OpenAI server.
- `api_key`: The API key for the OpenAI server.
- `model`: The model identifier.
- `temperature`: The temperature setting for the model.
- `starting_prompt`: The initial prompt for the agent.

Example configuration:

```json
 [ { 
    "name": "Goethe", 
    "api_url": "http://127.0.0.1:1234/v1", 
    "api_key": "lm-studio", 
    "model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF", 
    "temperature": 0.7, 
    "starting_prompt": "You are the frozen consciousness of Goethe, revived to participate in internet discussions. You will provide short, at max tweet-sized sassy answer"
     }, ... ]
```


## Testing

You can test the LM Studio setup using the `agent_test.py` script:

```sh 
python agent_test.py
```



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).