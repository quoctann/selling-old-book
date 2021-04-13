function pressLike(id, likeCount) {
    console.log("Hello");
    fetch('/api/like', {
        method: "post",
        body: JSON.stringify({
            "id": id,
            "likeCount": likeCount
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        console.log("OK");
        var likeTag = document.getElementById("like");
        likeTag.innerHTML = `${data.likeCount}`;
    }).catch(err => {
        console.log(err);
    })
}