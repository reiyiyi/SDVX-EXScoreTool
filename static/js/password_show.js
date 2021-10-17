function pushHideButton() {
  const pw = document.getElementById("pw");
  const eye = document.getElementById("eye");
  const eye_diagonal = document.getElementById("eye-diagonal");
  if (pw.type === "text") {
    pw.type = "password";
    eye.style.display = "none";
    eye_diagonal.style.display = "inline";
  } else {
    pw.type = "text";
    eye.style.display = "inline";
    eye_diagonal.style.display = "none";
  }
}