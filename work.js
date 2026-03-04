<html>
<body>
<h1>JavaScript Functions</h1>
<h2>The return Statement</h2>
<p>A function that performs a calculation and returns the result:</p>

<p id="demo"></p>

<script>
function myFunction(a, b) {
  return a * b;
}

let x = myFunction(4, 3);

document.getElementById("demo").innerHTML = "The product is " + x;
</script>

</body>
</html>
