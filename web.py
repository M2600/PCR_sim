from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import check_match

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        forward_primary = request.json['forward']
        reverse_primary = request.json['reverse']
        sequence = request.json['sequence']
        threshold = request.json['threshold']
        
        forward_primary = check_match.get_dna_complement(forward_primary.upper())
        reverse_primary = check_match.get_dna_complement(reverse_primary.upper()[::-1])
        sequence = sequence.upper()

        forward_match_indexes = check_match.check(forward_primary, sequence, float(threshold))
        reverse_match_indexes = check_match.check(reverse_primary, sequence, float(threshold))

        match_forwards = []
        for index in forward_match_indexes:
            match_forwards.append(sequence[index:index+len(forward_primary)])
        match_reverses = []
        for index in reverse_match_indexes:
            match_reverses.append(sequence[index:index+len(reverse_primary)])
        sequences = []
        for f_index in forward_match_indexes:
            for r_match in reverse_match_indexes:
                if f_index < r_match:
                    sequences.append(sequence[f_index:r_match+len(reverse_primary)])
        res = {
            'sequence': sequence,
            'threshold': threshold,
            'forward_indexes': forward_match_indexes,
            'reverse_indexes': reverse_match_indexes,
            'forward_primary': forward_primary,
            'reverse_primary': reverse_primary,
            'match_forwards': match_forwards,
            'match_reverses': match_reverses,
            'sequences': sequences
        }
        return jsonify(res)



