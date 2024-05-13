// import imageResize from 'quill-image-resize';
//import axios from 'axios';

// Quill.register('modules/imageResize', ImageResize);
function sen(s){
  // данные для отправки
//  var data = JSON.stringify({ "author": "aboba", "text": s.toString() });
//
//  let response = await fetch('http://localhost:8008/add', {
//        method: 'POST',
//        headers: {
//            'Content-Type': 'application/json;'
//        },
//        body: JSON.stringify({author: "aboba", text: "toString(s)" })
//    }) ;


const author = "John Doe";
const text = "This is a sample text.";

// Create the JSON object
const data = {
  author: author,
  text: text
};

// Convert JSON to string
const jsonData = JSON.stringify(data);

// URL of your FastAPI endpoint
const url = "http://localhost:8000/add";

// Send POST request with JSON data
fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: jsonData,
})
.then(response => response.json())
.then(data => console.log('Success:', data))
.catch((error) => console.error('Error:', error));

// Assuming you have the author and text ready
//const author = "John Doe";
//const text = "This is a sample text.";
//
//// Create the JSON object
//const data = {
//  author: author,
//  text: text
//};
//
//// URL of your FastAPI endpoint
//const url = "http://localhost:8000/your-endpoint";
//
//// Send POST request with JSON data
//axios.post(url, data)
//  .then((response) => {
//    console.log(response.data);
//  })
//  .catch((error) => {
//    console.error(error);
//  });
//


//    reques = await response.json();
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
//  xhr.open("POST", "./add");
////  setRequestHeader("Content-Type", "application/json");
//  alert(data)
//  xhr.send(data);     // отправляем значение user в методе send
}

// sen('dfsdfsdfsdfsdfsdf')

const quill = new Quill('#editor', {
    modules: {
      syntax: true,
      toolbar: '#toolbar-container',
      // handlers: {
      //   'image': imageHandler
      // },
    },
    placeholder: 'Compose an epic...',
    theme: 'snow',
  });
  
  document.querySelector('#q').addEventListener('click', () =>{
    let delta = quill.getSemanticHTML();
    // let u = delta.indexOf('<img')
    // let y = delta.slice[u].indexOf('</img')
    sen(delta);
})






const toolbar = quill.getModule('toolbar');
toolbar.addHandler('image', showImageUI);




// var quill = new Quill('#editor', {
//   theme: 'snow',
//    modules: {
//       imageDrop: true,
//       imageResize: {
//         displaySize: true
//       }
//   }
// });

