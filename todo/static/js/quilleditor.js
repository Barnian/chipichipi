// import imageResize from 'quill-image-resize';

// Quill.register('modules/imageResize', ImageResize);
function sen(s){
  // данные для отправки
  const user = s;
  
  const xhr = new XMLHttpRequest();
  
  // обработчик получения ответа сервера
  xhr.onload = () => {
      if (xhr.status == 200) { 
          console.log(xhr.responseText);
      } else {
          console.log("Server response: ", xhr.statusText);
      }
  };
 
// POST-запрос к ресурсу /user
  xhr.open("POST", "./add");
  xhr.send(toString(user));     // отправляем значение user в методе send
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

