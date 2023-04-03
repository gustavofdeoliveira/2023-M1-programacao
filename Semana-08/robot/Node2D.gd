extends Node2D

func _process(delta):
	$HTTPRequest.request("http://127.0.0.1:5000/coordinate/listOne", [], false, HTTPClient.METHOD_GET)	

func _on_HTTPRequest_request_completed(result, response_code, _headers, body):
	if result == HTTPRequest.RESULT_SUCCESS:
		var json = JSON.parse(body.get_string_from_utf8())
		var coordinateX = int(json.result["coordinateX"])
		var coordinateY = int(json.result["coordinateY"])
		var coordinateZ = int(json.result["coordinateZ"])
		$Sprite.position.x = coordinateX * 5
		$Sprite.position.y = coordinateY * 5
		$Sprite.scale.x = coordinateZ
		$Sprite.scale.y = coordinateZ
		$CanvasLayer/CoordinateX.text = str(coordinateX * 5)
		$CanvasLayer/CoordinateY.text = str(coordinateY * 5)
		$CanvasLayer/CoordinateZ.text = str(coordinateZ * 5)
		print($Sprite.position)
	else:
		print("Error: ", response_code)
