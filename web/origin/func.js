var curMode = 0;
function postCmd( str )
{
  if ( str === "" )
	return;
  jsonCmd = {"SENDCMD":str};
  console.log(jsonCmd);
  w.postMessage(jsonCmd);		
}

function execCmd(id)
{
  editCmd = 0;
  str=$(id).value;
  $(id).value = '';
  ( str.indexOf( "clear msg" )  === 0 ) ?  $( 'tx' ).value="" :	  
	postCmd( str );
}
function showSYS( data )
{
	len = data[1];
	len <<= 8;
	len += data[2];
	if( len  < 4 )
		return;
	lt = 0;
	//get lifetimr
	for( i = 3 ; i < 7; ++i )
	{
		lt <<= 8;
		lt += data[i];
	}	
	$( 'LT' ).innerHTML = lt;
	if( len < 32 )
		return;
	// get softwareserial baudrate
	ssbps = 0;
        for( i = 32 ; i < 36; ++i )
	{
		ssbps <<= 8;
		ssbps += data[i];
	}
	$( 'SSbps').innerHTML = ssbps;

}
function showEEPROM( data )
{
	var str = "\t";
	for( i=0; i<16; ++i)
	{
		str += ( i < 16 ) ? "x" :"";
		str += i.toString( 16 );
		str += '\t';
	}
	str += '\n';
	ptr = 3;
	for( i=0; i<20 ; ++i )
	{
		str += ( i < 16 ) ? "0" : "";
		str += i.toString(16);
		str += 'x';
		str += '\t';
		for( j=0; j<16; ++j )
		{
			var k = data[ptr++];
			str += ( k < 16 ) ? "0" : "";
			str += k.toString( 16 );
			str += '\t';
		}
		str += '\n';	
	}
	$( 'tx' ).value = str;
}

function showUserData( data )
{	

}

