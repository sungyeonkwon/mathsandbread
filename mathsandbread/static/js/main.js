console.log('main.js')

const JS_STACK_MAX_HEIGHT = '40px';

const handleJsStackClick = jsStack => {
  if (![...jsStack.classList].includes('show')) {
    applyJsStackTotalHeight(jsStack)
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
  } else {
    return;
  }
  handleJsStackClick(jsStack)
  return;
}

const applyJsStackTotalHeight = jsStack => {
  const titleHeight = jsStack.querySelector('.title').clientHeight
  const contentHeight = jsStack.querySelector('.content').clientHeight
  jsStack.style.maxHeight = `${titleHeight + contentHeight}px`
}

const handleReSize = () => {
  jsStacks.forEach( v => {
    if ([...v.classList].includes('show')) {
      applyJsStackTotalHeight(v)
      return;
    } 
  })
}

const handleFirstStack = () => {
  applyJsStackTotalHeight(jsStacks[0])
}

const jsStacks = document.querySelectorAll('.js-stack');

const addEventListeners = () => {
  window.addEventListener('resize', handleReSize)
  window.addEventListener('load', handleFirstStack)
  jsStacks.forEach(stack => {
    stack.addEventListener('click', onStackClick)
  })  
}

addEventListeners()