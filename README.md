# gdpr_regex

Tool to detect potentially sensitive data in text using regular expressions.

- Tested on the [CUAD dataset](https://www.atticusprojectai.org/cuad) of English contracts.

- Aimed at high recall, at the cost of many false positives


## Requirements

Python 3.8+


## Sample usage

Process single file, print all matches:

```
python main.py --file sample_data_small.txt
```

Run in quiet mode on larger text, print summary stats only:

```
python main.py --file sample_data_large.txt -q
```

```
done, processed 330.3KiB text in 0:00:00.398533, found 4110 matches
most common categories: [('named entity', 2294), ('date', 1708), ('computer address/url', 46), ('other', 33), ('phone number', 29)]
```

Running on the full CUAD dataset:

```
python main.py --path ~/projects/cdl/data/CUAD_v1/full_contract_txt/ -q
```

```
processed 36.5MiB text in 0:00:33.258414, found 328556 matches
```

Note that speed could be increased considerably by optimizing regular expressions.




