# HR Assistant AI Agent

HR Assistant AI Agent is an intelligent, automated HR support tool designed to streamline human resources operations. It leverages advanced AI models (Claude) via the Model Context Protocol (MCP) to provide features like answering HR queries, fetching employee information, and assisting with HR processes directly from your desktop.

## Features

AI-driven HR Support – Answer employee queries about leave policies, benefits, onboarding, and more.

File System Integration – Access and manage HR-related documents securely.

Google Maps Integration – Fetch location-based information for offices or branches.

Modular Architecture – Built on MCP for easy extension with new tools and endpoints.

Cross-platform – Works on Windows, macOS, and Linux with Python.

## Tech Stack

Python 3.12+ – Core backend logic

Agno – Agent orchestration and automation framework

MCP (Model Context Protocol) – Connects AI models with your tools

Claude Desktop – AI inference engine

Google Maps API – Location services

FastMCP – Lightweight Python MCP server

## Installation
### Prerequisites

Python 3.12 or higher installed.

Git installed on your system.

(Optional) Node.js if using MCP servers that require npm packages.

### Steps

Clone this repository:

git clone https://github.com/RukmalRt/HR-Assistant-Agent.git
cd HR-Assistant-Agent


### Create and activate a Python virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


### Install Python dependencies:

pip install -r requirements.txt

Running the Server

Start the MCP servers and your HR assistant agent:

python server.py


### You should see logs indicating that:

atliq-hr-assist server started successfully

google-maps MCP server connected

Filesystem access server initialized

Once running, the agent can receive requests and provide HR assistance.

## Usage

Query the agent: Send requests via the MCP protocol or your preferred client.

Manage HR documents: Use filesystem tools exposed by MCP (read_file, write_file, etc.).

Geolocation services: Use maps_geocode or maps_reverse_geocode for office locations.

## Example:

import requests

response = requests.post("http://localhost:8000/health")
print(response.json())

## Contributing

We welcome contributions!

Fork the repository

Create a feature branch: git checkout -b feature/awesome-feature

Commit your changes: git commit -m "Add awesome feature"

Push to the branch: git push origin feature/awesome-feature

Create a pull request

## Troubleshooting

Server disconnected / transport closed: Ensure the Python MCP server is running and the correct Python version is used.

Validation errors (like URLs in MCP resources): Use absolute or fully qualified paths for resources instead of simple strings.

Dependencies issues: Run pip install -r requirements.txt in a clean virtual environment.

## License

MIT License © 2025 Rukmal Rt
