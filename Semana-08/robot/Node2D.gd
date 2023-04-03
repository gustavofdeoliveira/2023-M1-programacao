extends Node2D  # This script extends the Node2D class

func _process(delta):  # This function is called every frame to update the node's state
	$HTTPRequest.request("http://127.0.0.1:5000/coordinate/listOne", [], false, HTTPClient.METHOD_GET)
	# Sends an HTTP request to the specified URL to retrieve coordinate data 

func _on_HTTPRequest_request_completed(result, response_code, _headers, body):  # This function is called when the HTTP request is completed
	if result == HTTPRequest.RESULT_SUCCESS:  # Checks if the request was successful
		var json = JSON.parse(body.get_string_from_utf8())  # Parses the JSON data received from the response body
		var coordinateX = int(json.result["coordinateX"])  # Extracts the X coordinate value from the JSON data
		var coordinateY = int(json.result["coordinateY"])  # Extracts the Y coordinate value from the JSON data
		var coordinateZ = int(json.result["coordinateZ"])  # Extracts the Z coordinate value from the JSON data
		$Sprite.position.x = coordinateX * 5  # Sets the X position of the Sprite node based on the retrieved X coordinate value
		$Sprite.position.y = coordinateY * 5  # Sets the Y position of the Sprite node based on the retrieved Y coordinate value
		$Sprite.scale.x = coordinateZ  # Sets the X scale of the Sprite node based on the retrieved Z coordinate value
		$Sprite.scale.y = coordinateZ  # Sets the Y scale of the Sprite node based on the retrieved Z coordinate value
		$CanvasLayer/CoordinateX.text = str(coordinateX * 5)  # Displays the X coordinate value on the UI
		$CanvasLayer/CoordinateY.text = str(coordinateY * 5)  # Displays the Y coordinate value on the UI
		$CanvasLayer/CoordinateZ.text = str(coordinateZ * 5)  # Displays the Z coordinate value on the UI
		print($Sprite.position)  # Prints the current position of the Sprite node
	else:
		print("Error: ", response_code)  # Prints an error message if the HTTP request fails
