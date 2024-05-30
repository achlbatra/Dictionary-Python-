
# VerbaVis 📖

VerbaVis is a simple and interactive dictionary application built with Streamlit. It allows users to look up the definitions of words and provides suggestions for close matches if the exact word is not found.

## Features

- **Word Lookup**: Enter a word to get its definition.
- **Case Insensitivity**: Handles words in different cases (lowercase, uppercase, title case).
- **Close Matches**: Suggests close matches if the word is not found in the dictionary.
- **Interactive UI**: Clear and user-friendly interface with a "Rerun" button to reset and restart the application.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/verba-vis.git
    cd verba-vis
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Add your dictionary data**:
    - Place your `data.json` file in the project directory. Ensure it is a valid JSON file with word definitions.

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

2. **Open your web browser**:
    - Go to `http://localhost:8501` to view the application.

## Project Structure

```
verba-vis/
├── data.json            # Your dictionary data in JSON format
├── app.py               # Main Streamlit application file
├── requirements.txt     # List of required Python packages
└── README.md            # This README file
```

## Example `data.json` Format

```json
{
    "example": ["A representative form or pattern", "Something that serves to illustrate or explain a rule"],
    "word": ["A single distinct meaningful element of speech or writing"]
}
```

## Customization

- **CSS Styling**: Custom styles are added to hide scrollbars and style the header.
- **Functionality**: Modify the `findMeaning` function in `app.py` to change how word meanings are retrieved or how suggestions are handled.

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-new-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-new-feature`.
5. Submit a pull request.


## Acknowledgments

- Thanks to the Streamlit team for creating such an amazing tool for building web apps with Python.
- Special thanks to the contributors of the difflib module in Python.
