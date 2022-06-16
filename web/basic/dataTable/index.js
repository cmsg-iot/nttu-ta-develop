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

window.wkMsg = function wkMsg(e) {
  try {
    if (e.data instanceof Uint8Array) {
      e.data[0] === 0x00
        ? showSYS(e.data)
        : e.data[0] === 0x01
        ? showEEPROM(e.data)
        : 0;
    }

    if (window.dataFormatEntryPoint !== undefined) {
      window.dataFormatEntryPoint(e.data);
    }

    if (e.data.RSSI === "<---->") {
      window.lost++;
    } else if (e.data.RSSI) {
      window.lost--;
    }

    if (window.lost > 1) {
      window.lost = 1;
      console.log("lost connection");
      $("status_light").classList.remove("light-green");

      if (!flag_lost) {
        flag_lost = true;
        alert("連接異常，請重新整理網頁、檢查Wifi或重啟設備。");
      }
    } else {
      flag_lost = false;
      $("status_light").classList.add("light-green");
    }
  } catch (error) {
    console.log(error);
  }
};

function showSYS(data) {
  len = data[1];
  len <<= 8;
  len += data[2];
  if (len < 4) return;
  lt = 0;
  //get lifetimr
  for (i = 3; i < 7; ++i) {
    lt <<= 8;
    lt += data[i];
  }
  //   $("LT").innerText = lt;
  window.current_LT = lt;
  if (len < 32) return;
  // get softwareserial baudrate
  ssbps = 0;
  for (i = 32; i < 36; ++i) {
    ssbps <<= 8;
    ssbps += data[i];
  }
}

function showEEPROM(data) {
  var str = "\t";
  for (i = 0; i < 16; ++i) {
    str += i < 16 ? "x" : "";
    str += i.toString(16);
    str += "\t";
  }
  str += "\n";
  ptr = 3;
  for (i = 0; i < 20; ++i) {
    str += i < 16 ? "0" : "";
    str += i.toString(16);
    str += "x";
    str += "\t";
    for (j = 0; j < 16; ++j) {
      var k = data[ptr++];
      str += k < 16 ? "0" : "";
      str += k.toString(16);
      str += "\t";
    }
    str += "\n";
  }
  $("tx").value = str;
}

// 定義函式，給定最小與最大值，回傳範圍中的隨機整數
function getRadomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
}

// 模擬資料更新
// setInterval(function () {
//   // 模擬原始資料(JSON字串)
//   var fakeData = `{"ax":${getRadomInt(-18000, 18000)},"ay":${getRadomInt(
//     -18000,
//     18000
//   )},"az":${getRadomInt(-18000, 18000)},"gx":${getRadomInt(
//     -18000,
//     18000
//   )},"gy":${getRadomInt(-18000, 18000)},"gz":${getRadomInt(-18000, 18000)}}`;

//   // 在DevTools印出 fakeData 內容
//   console.log(fakeData);

//   // 將JSON字串轉換成JSON物件
//   var fakeData_json = JSON.parse(fakeData);

//   // 在DevTools印出 fakeData_json 內容
//   console.log(fakeData_json);

//   // 利用id名稱取得DOM物件，利用innerText方法插入數值
//   // 利用 變數.key 的方式取得JSON物件中的資料，如 fakeData_json.ax 取得 ax 中的值
//   document.getElementById("ax").innerText = fakeData_json.ax;
//   document.getElementById("ay").innerText = fakeData_json.ay;
//   document.getElementById("az").innerText = fakeData_json.az;
//   document.getElementById("gx").innerText = fakeData_json.gx;
//   document.getElementById("gy").innerText = fakeData_json.gy;
//   document.getElementById("gz").innerText = fakeData_json.gz;
// }, 1000);
