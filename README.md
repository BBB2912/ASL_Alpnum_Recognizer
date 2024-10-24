**Sign Language ASL Alphanumeric Recognizer**
============================================

Welcome to the **ASL\_Alpha\_Recognizer** project! This repository provides a robust solution for recognizing American Sign Language (ASL) alphabetic and numeric signs. With two core scripts (recognizer.py and recognizer1.py), you can recognize individual ASL signs and even suggest full words based on gestures!

Features
--------

1.  **Alphabet and Numeric Recognition**:
    
    *   This project supports recognition of **all alphanumeric signs (A-Z, 0-9)**.
        
    *   The core recognizer script, recognizer.py, helps you identify individual signs with ease.
        
2.  **Word Suggestion Mode**:
    
    *   The script recognizer1.py takes it a step further by integrating a word suggester.
        
    *   It utilizes an **NLTK-based word database with 23,000 words** to provide smart suggestions.
        
    *   Simply make the 'Z' sign to switch between **alphabet mode** and **word suggestion mode**.
        

Getting Started
---------------

### Prerequisites

*   Python 3.x
    
*   bashCopy codepip install opencv-python tensorflow keras nltk
    

### Setup

1.  bashCopy codegit clone https://github.com/your\_username/ASL\_Alpha\_Recognizer.gitcd ASL\_Alpha\_Recognizer
    
2.  **Run the Recognition Script**:
    
    *   bashCopy codepython recognizer.py
        
3.  **Run the Word Suggestion Script**:
    
    *   bashCopy codepython recognizer1.py
        

### Dataset

To train the model on alphanumeric ASL signs, refer to the publicly available dataset:Alphabets: [https://www.kaggle.com/datasets/grassknoted/asl-alphabet](https://www.kaggle.com/datasets/grassknoted/asl-alphabet)

Numerics: [https://www.kaggle.com/datasets/lexset/synthetic-asl-numbers](https://www.kaggle.com/datasets/lexset/synthetic-asl-numbers)

The dataset contains labeled images of all ASL alphabet signs, which are essential for recognizing gestures accurately.

How to Use
----------

1.  **ASL Recognition (recognizer.py)**:
    
    *   Once the script is running, show any ASL sign (A-Z, 0-9) in front of the camera, and it will predict the letter or number.
        
2.  **ASL Word Suggestion Mode (recognizer1.py)**:
    
    *   Show the **Z sign** to switch to word suggestion mode.
        
    *   In this mode, you can continue signing letters, and the system will suggest words based on the signed letters using a 23,000-word dataset.
        
    *   Use the suggestions to form complete words by choosing from the displayed options.
        

Customization
-------------

*   You can expand the word suggestion list or improve the gesture recognition accuracy by adding more data or retraining the model using the provided dataset.
    

Contributing
------------

Feel free to contribute to this project! Whether it's adding new features, improving recognition accuracy, or adding more robust datasets, you're welcome to submit pull requests.
License
-------

This project is licensed under the MIT License.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   markdownCopy code  ### Notes:  - Replace `YourUsername` with your actual GitHub username.  - Ensure the `requirements.txt` reflects the actual dependencies your project uses.  - Make sure to test the project after removing the `maxTrackCon` argument, as outlined in the "Known Issues" section.   ``
