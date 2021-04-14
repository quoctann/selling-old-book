function pressLike(id, likeCount) {
    console.log("ID: " + id + "; Count: " + likeCount);
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
        var likeTag = document.getElementById("like" + id);
        likeTag.innerHTML = `${data.likeCount}`;
    }).catch(err => {
        console.log(err);
    })
}