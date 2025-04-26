# Financial Report Summarization for Financial Advisors

## Project Overview

This project creates an AI-based solution to generate concise 1-page and 2-page summaries of financial analyst reports and 10-K reports, simplifying the process of understanding a company's financial position.

## Features

- Extracts relevant data from multiple financial analyst reports and 10-K documents.
- Generates well-formatted 2-page summaries including:
  - Business Overview
  - Business Segment Overview
  - Performance Analysis
  - Geographical Sales Breakdown
  - Regional Sales Analysis
  - Year-over-Year Sales Analysis
  - Rationale & Considerations
  - SWOT Analysis
  - Credit Rating Information
- Generates a concise 1-page summary from the 2-page summary.
- Uses OpenAI API for text summarization and embedding generation.
- Employs ChromaDB for efficient embedding storage and retrieval.
- Streamlit-based user interface for uploading PDFs and downloading generated summaries.


## Installation


1. **Create and activate a virtual environment:**
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows: venv\Scripts\activate

2. **Install required packages:**
    ```bash
    pip install -r requirements.txt

3. **Set up OpenAI API key:**
    Create a .env file in the root directory and add:
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    CHROMADB_PERSIST_DIRECTORY=./chroma_db
    NUM_CLUSTERS=5



## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Upload PDF files and generate summaries using the web interface.**
- `Output`: For a more comprehensive and formatted version of the summaries, please visit the project's output folder.

## Additionals: 
## Comprehensive Testing


1. **Run All Tests by running this command in the terminal:**
   ```bash
   python run_tests.py

2. **Expected Results:**
    ```bash 
    test_full_workflow (test_app.TestAppIntegration) ... ok
    test_save_to_docx (test_docx_utils.TestDocxUtils) ... ok
    test_extract_text (test_pdf_extractor.TestPDFExtractor) ... ok
    test_chunk_text (test_text_processor.TestTextProcessor) ... ok
    test_enhance_text_with_nlp (test_text_processor.TestTextProcessor) ... ok
    test_format_text (test_text_processor.TestTextProcessor) ... ok
    test_preprocess_text (test_text_processor.TestTextProcessor) ... ok
    
    Ran 7 tests in 23.241s
    
    OK
    All test cases ran successfully




## Key Modules
- `chromadb_utils.py`: Manages ChromaDB operations, including creating collections, adding embeddings, and querying the database. Supports specifying a persistent directory to avoid conflicts. This module is crucial for efficient storage and retrieval of document embeddings.

- `config_manager.py`: Handles configuration settings by loading environment variables and providing configuration data to other modules. Ensures consistent configuration across the application.

- `docx_utils.py`: Handles DOCX file creation and formatting. Saves text summaries as well-structured Word documents, adjusts document margins, and adds formatted paragraphs. Ensures consistent styling and layout for the financial reports.

- `logging_config.py`: Sets up logging configurations to ensure consistent logging across the application, including custom filters. Facilitates effective debugging and monitoring of the application.

- `openai_utils.py`: Interfaces with the OpenAI API, handling requests for text summarization and embedding generation. Includes comprehensive error handling. This module encapsulates all interactions with OpenAI's language models and embedding services.

- `pdf_extractor.py`: Extracts text from PDF files using pdfplumber. Processes various types of financial documents, including handling of tables within PDFs. Capable of dealing with complex layouts to provide clean text for further analysis.

- `templates.py`: Contains templates for generating structured summaries. Provides detailed and concise summary templates for financial reports, ensuring consistency in output format.

- `text_processor.py`: Processes and formats text data. Cleans and normalizes text, formats text with headings and bold sections, enhances text with NLP techniques, and chunks large documents into manageable sizes. This module is essential for preparing text for summarization and analysis.

## Code Design Principles
###  ** (IMPORTANT: EXPLICITLY MENTIONED FOR EVALUATION) **

### Modularity
The project codebase is structured to ensure that each function and class performs a single, well-defined task. This approach enhances maintainability and testability by promoting separation of concerns and reducing dependencies between different parts of the code. Functions are designed to be reusable and independent, facilitating easier debugging and updates.

### Single Responsibility Principle
Adhering to the Single Responsibility Principle (SRP), each module, class, and function within the project has a single responsibility. This design choice simplifies the codebase, making it more understandable and maintainable. It ensures that changes to one part of the code do not inadvertently affect other parts, thus reducing the risk of bugs.

### Error Handling
Comprehensive error handling mechanisms are implemented throughout the project to ensure robustness and reliability. The use of try-except blocks around critical operations, such as file I/O and API requests, ensures that potential errors are caught and handled gracefully. This prevents the application from crashing and provides meaningful error messages to the user.

### Configuration Management
To enhance flexibility and maintainability, the project avoids hardcoded paths and magic numbers. Instead, configurations are managed through parameters and environment variables. This approach allows the application to be easily adapted to different environments and requirements without modifying the code.

### Documentation
The code is thoroughly documented with clear and concise comments and docstrings. Each function and class includes explanations of its purpose, parameters, and return values. This documentation aids in understanding the code and ensures that future developers can easily work with the project.

### Testing
The project includes comprehensive unit tests to verify the functionality of individual components. Tests cover a wide range of scenarios, including edge cases and invalid inputs, to ensure the robustness of the code. The use of automated testing tools facilitates continuous integration and helps maintain code quality over time.

### Conclusion
By adhering to these software engineering principles, the project ensures a high standard of code quality, reliability, and maintainability. These principles are integral to the design and implementation of the project, providing a solid foundation for current and future development.


## Potential Issues and How They Were Dealt With
#### 1. Handling Different PDF Structures
Issue: Varying layouts in financial documents.

Solution: Used pdfplumber to robustly handle different PDF structures, including tables and multi-column layouts.

#### 2. Error Handling and Robustness
Issue: Potential errors from file uploads to API call failures.

Solution: Added comprehensive error handling and validation to manage exceptions and provide informative error messages.

#### 3. Managing Large Text Data
Issue: Performance issues with large financial documents.

Solution: Implemented text chunking and NLP techniques to break down large documents into manageable pieces for efficient processing.

#### 4. Ensuring Consistent Configurations
Issue: Inconsistent settings across modules.

Solution: Centralized configuration management using ConfigManager for consistent settings and avoiding conflicts.

#### 5. Testing and Validation
Issue: Ensuring code reliability.

Solution: Developed unit and integration tests for critical functions, using a custom test runner to validate functionality.

#### 6. Streamlining User Interface
Issue: Providing a user-friendly interface.

Solution: Used Streamlit to create an intuitive interface for file uploads and displaying results, including visual feedback and clear messages.


## Directory Structure
```bash 
    Project/
    ├── data/
    │   ├── Apple_10K.pdf
    │   ├── Apple_10Q.pdf
    │   └── Apple_Deautsche_Jun23.pdf
    │   └── Apple_JPM_Jun23.pdf
    ├── myenv/
    ├── output/
    │   ├── summary1page.docx
    │   └── summary2page.docx
    ├── src/
    │   ├── chromadb_utils.py
    │   ├── config_manager.py
    │   ├── docx_utils.py
    │   ├── logging_config.py
    │   ├── openai_utils.py
    │   ├── pdf_extractor.py
    │   ├── templates.py
    │   └── text_processor.py
    ├── tests/
    │   ├── Apple_10Q.pdf
    │   ├── test_app.py
    │   ├── test_docx_utils.py
    │   ├── test_pdf_extractor.py
    │   └── test_text_processor.py
    ├── .env
    ├── app.log
    ├── app.py
    ├── README.md
    ├── requirements.txt
    └── run_tests.py


## Example Input and Output
#### Input:
Apple_10K.pdf, 

Apple_10Q.pdf, 

Apple_Deautsche_Jun23.pdf, 

Apple_JPM_Jun23.pdf

#### Output:
#### 2-Page Summary:

Business Overview:

Apple Inc., founded in April 1, 1976.
Headquarters in Cupertino, California.

Technology company focused on designing, manufacturing, and marketing consumer electronics, computer software, and online services.
Approximately 164,000 employees.

Listed on NASDAQ (AAPL) with a market capitalization of approximately $2.7 trillion.
International presence with offices in over 25 countries.

and so on...

---

#### 1-Page Summary:

Business Overview:

Apple Inc., key figures: founded in 1976, headquartered in Cupertino, California, approximately 164,000 employees. 

Business Segment Overview:

Segments and revenue percentages: iPhone 58.2%, Services 19.3%, other products 22.5%.

and so on...

## Feedabck

I would love to get more feedback on this project, reach me out anytime. Peace


.