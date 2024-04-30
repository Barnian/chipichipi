//function send(){
//    // данные для отправки
//  const email = document.getElementsByClassName("inp")[0].textContent;
//  const password = document.getElementsByClassName("inp")[0].textContent;
////  alert(email, password)
//  const xhr = new XMLHttpRequest();
//
//  // обработчик получения ответа сервера
//  xhr.onload = () => {
//      if (xhr.status == 200) {
//          console.log(xhr.responseText);
//      } else {
//          console.log("Server response: ", xhr.statusText);
//      }
//  };
//
//// POST-запрос к ресурсу /user
//  xhr.open("POST", "http://0.0.0.0:8008/authentification");
//  xhr.send(email);     // отправляем значение user в методе send
//}

async function send(){
    // данные для отправки
  const email = document.getElementsByClassName("inp")[0].value;
  const password = document.getElementsByClassName("inp")[1].value;
//   alert([email, password])
//   const xhr = new XMLHttpRequest();

//   // обработчик получения ответа сервера
//   xhr.onload = () => {
//       if (xhr.status == 200) {
//           console.log(xhr.responseText);
//       } else {
//           console.log("Server response: ", xhr.statusText);
//       }
//   };

// // POST-запрос к ресурсу /user
//   xhr.open("POST", "http://0.0.0.0:8008/add");
    let response = await fetch('http://0.0.0.0:8008/authentification', {
        method: 'POST',
        headers: {
'Accept': 'application/json',
'Content-Type': 'application/json'
},
body: JSON.stringify({"email": email, "psw": password}),
    }) ;
    reques = await response.json();
//   xhr.send([email, password]);     // отправляем значение user в методе send
}
