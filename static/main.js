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

function showCommentBox() {
  let commentArea = document.getElementById("comment-area");
  if (commentArea.style.display === "none")
    commentArea.setAttribute("style", "display:block");
  else
    commentArea.setAttribute("style", "display:none");
}

function showReplyBox(id) {
  let replyArea = document.getElementById(id);
  if (replyArea.style.display === "none")
    replyArea.setAttribute("style", "display:block");
  else
    replyArea.setAttribute("style", "display:none");
}