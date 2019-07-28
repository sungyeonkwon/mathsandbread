console.log('main.js')

// const fadeMessage = () => {
//   setTimeout(() => {
//     document.querySelector('#message').classList.add('hide')
//   }, 2000)
// }

const toggleContentClass = content => {
  return [...content.classList].includes('show')?
  content.classList.remove('show'):
  content.classList.add('show');
}

const onStackClick = e => {
  const classList = [...e.target.classList]
  let content;
  if (classList.includes('row')){
    content = e.target.nextElementSibling
  } else if(classList.includes('column')){
    content = e.target.parentElement.nextElementSibling
  } else if(classList.includes('quiz')){
    content = e.target.parentElement.parentElement
  }
  console.log("e.target", e.target.parentElement.parentElement)
  console.log("content", content)
  toggleContentClass(content)
  return;
}

const jsStacks = document.querySelectorAll('.js-stack');

jsStacks.forEach(stack => {
  stack.addEventListener('click', onStackClick)
})

