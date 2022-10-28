# gdpr_regex

The dataset has been tested on the [CUAD dataset](https://www.atticusprojectai.org/cuad).

It is known, that the name category has a lot of false positives.

## Usage

You can use the system on text files:

```
python main.py --file TEXT_FILE [TEXT_FILE ...]
```

Paths containing text files:

```
python main.py --path PATH_TO_DIRECTORY_WITH_TEXT_FILES [PATH_TO_DIRECTORY_WITH_TEXT_FILES ...]
```

Or simple strings in the command line:

```
python main.py --string STRING_IN_QUESTION
```

The output will contain warnings if the texts contain any sensitive data. For example:

"UserWarning: There might be sensitive information in the text! "The Night" could be a(n) named entity!"
