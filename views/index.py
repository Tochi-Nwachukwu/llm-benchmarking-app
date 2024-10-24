html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>LLM Benchmark Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: black;
                color: white;
                text-align: center;
                padding: 1em 0;
            }
            main {
                max-width: 900px;
                margin: 20px auto;
                background: white;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: white;
            }
            p {
                line-height: 1.6;
            }
            footer {
                text-align: center;
                padding: 1em 0;
                background-color: black;
                color: white;
                position: absolute;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>LLM Benchmark Simulation</h1>
        </header>
        <main>
            <h1>LLM Simulation api for GPT 4, Llama and Gemini</h1>
            <p>This application benchmarks different Language Learning Models (LLMs) based on various metrics, such as:</p>
            <ul>
                <li>Time to First Token (TTFT)</li>
                <li>Tokens Per Second (TPS)</li>
                <li>End-to-End Request Latency (e2e_latency)</li>
                <li>Requests Per Second (RPS)</li>
            </ul>
            <p>Use this app to rank LLMs and view their performance results via the available API routes.</p>
            <p>Visit the <a href="/docs">API Documentation</a> for more information on available endpoints.</p>
        </main>
        <footer>
            <p>Built by Tochi Nwachukwu</p>
        </footer>
    </body>
    </html>
    """