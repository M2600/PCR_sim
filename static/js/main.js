



function main(){
	
	submitButton = document.getElementById("submit")
	submitButton.addEventListener("click", async function(){
		var  forward = document.getElementById("forward").value;
		var reverse = document.getElementById("reverse").value;
		var sequence = document.getElementById("sequence").value;
		var threshold = document.getElementById("threshold").value;

		var data = {
			"forward": forward,
			"reverse": reverse,
			"sequence": sequence,
			"threshold": threshold
		}
		console.log(data)

		await fetch('/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		}).then(response => response.json())
		.then(data => {
			console.log(data)
			
			document.getElementById('forwardInfo').innerHTML = data.forward_primary;
			document.getElementById('reverseInfo').innerHTML = data.reverse_primary;
			document.getElementById('sequenceInfo').innerHTML = data.sequence;
			document.getElementById('thresholdInfo').innerHTML = data.threshold;


			var primaryUl = document.getElementById('foundPrimarySequences');
			primaryUl.innerHTML = '';
			var reverseUl = document.getElementById('foundReverseSequences');
			reverseUl.innerHTML = '';

			for (var i = 0; i < data.match_forwards.length; i++){
				var li = document.createElement('li');
				li.appendChild(document.createTextNode(data.match_forwards[i] + " at: " + data.forward_indexes[i]));
				primaryUl.appendChild(li);
			}
			for (var i = 0; i < data.match_reverses.length; i++){
				var li = document.createElement('li');
				li.appendChild(document.createTextNode(data.match_reverses[i] + " at: " + data.reverse_indexes[i]));
				reverseUl.appendChild(li);
			}

			var sequencesUl = document.getElementById('foundSequencesUl');
			sequencesUl.innerHTML = '';
			for (var i = 0; i < data.sequences.length; i++){
				var li = document.createElement('li');
				li.appendChild(document.createTextNode(data.sequences[i]));
				sequencesUl.appendChild(li);
			}

		})
	})
}


main()
