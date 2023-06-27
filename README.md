# LEPOR: A Robust Evaluation Metric for Machine Translation with Augmented Factors
Python Package for a machine translation evaluation metric named LEPOR.

## Installation
Requirement: Python 3

**Install pip package**
```bash
pip install lepor
```
## How to Run
#### Calculate the LEPOR for sentences
If you want to check only one sentence:
```python
>>> from lepor import sentence_lepor
>>> reference = 'a bird is on a stone.'
>>> output = 'a stone on a bird.'

>>> sentence_lepor(reference, output)
0.736
```
If you want to check multiple hypothesis (several sentences):
```python
>>> from lepor import corpus_lepor
>>> corpus_lepor(references, outputs)
```
## In Case of Unexpected Outputs
Create an issue so i will be able to help you as soon as i can. If there are any suggestions or ideas for improvement, feel free to create an issue and generate PR.

## Contact
If you have more questions or ideas for collaboration contact the author [Ikram Ul Haq](mailto:ulhaqi12@gmail.com).

## References
<div class="csl-entry">Han, A. L. F., Wong, D. F., &#38; Chao, L. S. (2012). <i>LEPOR: A Robust Evaluation Metric for Machine Translation with Augmented Factors</i> (pp. 441–450). https://aclanthology.org/C12-2044</div>
