console.log('main.js')

const JS_STACK_MAX_HEIGHT = '40px';

const toggleContentClass = jsStack => {
  if (![...jsStack.classList].includes('show')) {
    const titleHeight = jsStack.querySelector('.title').clientHeight
    const contentHeight = jsStack.querySelector('.content').clientHeight
    jsStack.style.maxHeight = `${titleHeight + contentHeight}px`
    jsStack.classList.add('show')
    return;
  } 
  jsStack.style.maxHeight = JS_STACK_MAX_HEIGHT
  jsStack.classList.remove('show')
}

const onStackClick = e => {
  const classList = [...e.target.classList]
  let jsStack;
  if (classList.includes('row')){
    jsStack = e.target.parentElement
  } else if(classList.includes('column')){
    jsStack = e.target.parentElement.parentElement
  } else if(classList.includes('quiz')){
    jsStack = e.target.parentElement.parentElement.parentElement
  }
  toggleContentClass(jsStack)
  return;
}

const jsStacks = document.querySelectorAll('.js-stack');

jsStacks.forEach(stack => {
  stack.addEventListener('click', onStackClick)
})

