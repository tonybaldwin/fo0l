<?php

// random shakespearean insult generator 
// by tony baldwin | https://tonybaldwin.info
// live demo: http://tonyb.us/shakes
// released according to the terms of the Gnu Affero Public License

$h = array("artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish", "dankish", "dissembling", "droning", "errant", "fawning", "foul", "fobbing", "froward", "frothy", "fusty", "gleeking", "goatish", "gorbellied", "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "mammering", "mangled", "mewling", "naughty", "paunchy", "pribbling", "puking", "deboshed", "puny", "qualling", "rank", "reeky", "roguish", "ruttish", "saucy", "spleeny", "spongy", "surly", "tottering", "unmuzzled", "vain", "venomed", "villainous", "warped", "wayward", "weedy", "yeasty", "cullionly", "fusty", "caluminous", "wimpled", "burly-boned", "misbegotten", "odiferous", "poisonous", "fishified", "wart-necked");

$h1 = mt_rand(0, (count($h) -1));

$b = array("base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "deformed", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-griping", "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle", "headed", "ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered", "mocking", "motley-minded", "onion-eyed", "plume-plucked", "sodden-witted", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne", "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad", "spotted", "unchin-snouted", "weather-bitten", " whoreson", "malmsey-nosed", "rampallian", "lily", "livered", "scurvy-valiant", "brazen-faced", "unwash'd", "bunch-back'd", "leaden-footed", "muddy-mettled", "pigeon-liver'd", "scale-sided");

$b1 = mt_rand(0, (count($b) -1));

$c = array("apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon", "drudge", "flax-wench", "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "joithead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow", "miscreant", "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet", "varlot", "vassal", "whey-face", "wagtail", "knave", "blind-worm", "popinjay", "scullian", "jolt-head", " malcontent", "devil-monk", "toad", "rascal", "basket-cockle");

$c1 = mt_rand(0, (count($c) -1));

echo "<center><a href=\"https://tonybaldwin.info/page/blog/shakes\"><img src=\"http://tonybaldwin.homelinux.net/images/shakespeare.gif\"></a><br /><font size=\"6\">Thou $h[$h1], $b[$b1] $c[$c1]!</font><br /><br /><font size=\"4\"><a href=\"https://tonybaldwin.info/page/blog/shakes\">Have at thee, scoundrel!</a></font></center>";

$title = "Shakespearean Insults!";
$insult = "[size=20]Thou $h[$h1], $b[$b1] $c[$c1]![/size]
[url=https://tonybaldwin.info/page/blog/shakes]Shakespeare Insult Generator[/url]
#shakespeare #insults";

echo "<br />";
$o = '<a href="/rpost?f=&title=' . $title . '&body=' . urlencode($insult) . '">Share on RedMatrix!</a>';
echo $o;

?>
