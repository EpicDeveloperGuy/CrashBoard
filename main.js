function hideIconBar() {
  let iconBar = document.getElementById("iconBar");
  let navigation = document.getElementById("navigation");
  iconBar.setAttribute("style", "display:none");
  navigation.classList.remove("hide");
}

function showIconBar() {
  let iconBar = document.getElementById("iconBar");
  let navigation = document.getElementById("navigation");
  iconBar.setAttribute("style", "display:block");
  navigation.classList.add("hide")
}

function showReplyBox() {
  let replyArea = document.getElementById("reply-area");
  replyArea.setAttribute("style", "display:block");
}