var w;
var act;
var editCmd = 0;
var kM;
var paramCnt = 0;
function $(id) {
  return document.getElementById(id);
}

function connect() {
  if (typeof Worker === "undefined") {
    console.log("not support Worker");
    return;
  }
  if (typeof w === "undefined") {
    w = new Worker("./worker.js");
    w.onmessage = wkMsg;
  }
  cmd = { URL: document.URL };
  w.postMessage(cmd);
}
function wkMsg(e) {
  if (e.data instanceof Uint8Array) {
    e.data[0] === 0x00
      ? showSYS(e.data)
      : e.data[0] === 0x01
      ? showEEPROM(e.data)
      : e.data[0] === 0x02
      ? showUserData(e.data)
      : 0;
    return;
  }
  var ii;
  for (i in e.data) {
    if (i == "tx") {
      ii = $("tx");
      str = ii.value;
      str += "\n";

      if (typeof e.data[i] === "object") {
        str += JSON.stringify(e.data[i]);
      } else {
        str += e.data[i];
      }

      ii.value = str;
      ii.scrollTop = ii.scrollHeight;
      continue;
    }
    ii = $(i);
    if (ii) {
      ii.innerHTML = e.data[i];
    }
  }
}
function clearMsg() {
  $("tx").value = "";
}
