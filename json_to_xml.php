<?php

$ulazniJson = json_decode(file_get_contents('granter.json'), true);   //relativni path
$xml = new DOMDocument('1.0', 'utf-8');
$xml->formatOutput = true;


function parseArray($XMLArray, $levels) {
	global $xml;	
	$level = $xml->createElement('Jedinice');  //root element
	$levels = $levels->appendChild($level);
	foreach($XMLArray as $XMLKey => $XMLValue) {
		$level = $xml->createElement('Jedinica');
		$level->setAttribute('id', '');
		$levels->appendChild($level);
		//ime hr
		$levelIme = $xml->createElement('Ime', $XMLValue['name']['hr']);
		$level->appendChild($levelIme);
		$levelIme->setAttribute('lang', 'hr');
		//ime eng
		$levelIme = $xml->createElement('Ime', $XMLValue['name']['en']);
		$level->appendChild($levelIme);
		$levelIme->setAttribute('lang', 'en');
		//tip ustanove
		$levelTip = $xml->createElement('Tip', ($XMLValue['type']));
		$level->appendChild($levelTip);
		
		//provjera children elementa
		if (is_array($XMLValue['children'])) {		
			parseArray($XMLValue['children'], $level);
		}
	}
}


parseArray($json, $xml);


//echo '<pre>';

print_r($xml->saveXML());
//echo '</pre>';

?>