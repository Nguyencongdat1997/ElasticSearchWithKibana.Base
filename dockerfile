FROM python
ADD . /datgatto
WORKDIR /datgatto
RUN pip install -r python_requirement.txt
CMD ./input_data.py 