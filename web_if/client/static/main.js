const TITLE = "Variable Boot Drive";

function pinInput() {
  const loader = document.getElementById("loader");
  loader.classList.add("container-fluid", "p-0");
  // Create a form with a single password input called pin
  const form = addElement(loader, "form", [
    "pin-form",
    "row",
    "justify-content-center",
  ]);
  form.id = "pin-form";
  const inputGroup = addElement(form, "div", ["input-group", "mb-3"]);
  const input = addElement(inputGroup, "input", ["form-control"]);
  input.type = "password";
  input.id = "pin";
  input.name = "pin";
  input.placeholder = "Enter PIN";
  input.required = true;
  input.autocomplete = "off";

  // Submit button to run the "authenticate" function
  const submit = addElement(inputGroup, "button", ["btn", "btn-primary"]);
  submit.type = "submit";
  submit.textContent = "Submit";

  // Prevent default form submission
  form.addEventListener("submit", function(event) {
    event.preventDefault();
    const pinValue = input.value;

    // Call your authentication function instead of submitting the form
    authenticate(hash(pinValue));
  });
}

/**
 * 
 */
async function hash(pin) {
    const encoder = new TextEncoder();  // TextEncoder uses UTF-8 by default
    const data = encoder.encode(pin);
    const hashBuffer = await crypto.subtle.digest("SHA-256", data);
    return Array.from(new Uint8Array(hashBuffer))
        .map(byte => byte.toString(16).padStart(2, '0'))
        .join('');
}

async function authenticate(pinValue) {
  console.log(hash("1234"));
  // console.log(pinValue);
}

/**
 * Render the content of the website
 * return {void}
 */
function loadContent() {
  document.title = TITLE;
  renderHeader();
  renderMain();
  renderFooter();
}

/**
 * Render the header of the website.
 * Currently only renders the navbar.
 * There may be more content in the future.
 * return {void}
 */
function renderHeader() {
  const header = document.getElementById("header");
}

/**
 * Renders each section of the website.
 * return {void}
 */
function renderMain() {
  const main = document.getElementById("main");
  main.classList.add("container-fluid", "p-0");
  // Render Sections here
}

/**
 * Renders the footer of the website.
 * return {void}
 */
function renderFooter() {
  const footer = document.getElementById("footer");
  footer.classList.add(
    "container-fluid",
    "p-3",
    "bg-dark",
    "text-white",
    "text-center",
  );
  const footerRow = addElement(footer, "div", ["row"]);
  const copyright = addElement(footerRow, "div", ["col", "mx-auto"]);
  const footerImg = addElement(copyright, "img", ["p-0", "m-2"]);
  footerImg.src = "assets/footer-logo.png";
  footerImg.alt = "PLACEHOLDER NAME";
  footerImg.width = 28;
  footerImg.height = 35;
  const p = addElement(copyright, "span", ["p-0", "m-0"]);
  p.textContent = "© " + 2025 + " " + TITLE;
}

/**
 * Create an element with the given tag and classes.
 * Does not add it to the DOM immediately.
 * @param {String} tag - The tag of the element to create.
 * @param {Array} classes - The classes to add to the element.
 * return {HTMLElement} - The created element.
 */
function createElement(tag, classes = []) {
  const element = document.createElement(tag);
  if (classes.length > 0) element.classList.add(...classes);
  return element;
}

/**
 * Add an element to the parent element with the given tag and classes.
 * Immediately appends the element to the parent.
 * If the parent is in the DOM, the element will be as well.
 *
 * @param {HTMLElement} parent - The parent element to append the element to.
 * @param {String} tag - The tag of the element to create.
 * @param {Array} classes - The classes to add to the element.
 *
 * return {HTMLElement} - The created element.
 */
function addElement(parent, tag, classes = []) {
  const element = createElement(tag, classes);
  parent.appendChild(element);
  return element;
}

document.addEventListener("DOMContentLoaded", function() {
  pinInput();
  // loadContent();
});
