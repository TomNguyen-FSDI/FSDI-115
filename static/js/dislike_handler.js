
$('.dislike-container').submit(function(e){
    e.preventDefault();
    const post_id = $(this).attr('id');
    const url = $(this).attr('action');
    // like fron end vars and consts
    const likeClass = $(`.like-btn${post_id}`).children()[0].classList[2];
    console.log(likeClass);
    let likeRes;
    const likes = $(`.like-count${post_id}`).text();
    const trimCount = parseInt(likes);
    // dislikes front end vars and consts
    const dislikeClass = $(`.dislike-btn${post_id}`).children()[0].classList[2];
    

    let dislikeRes;
    const dislikes = $(`.dislike-count${post_id}`).text();
    const dislikeTrimCount = parseInt(dislikes);

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: url,
      data: {
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken').val(),
        'post_id': post_id,
      },
      success: function(response){
        console.log('success', response)
        if(dislikeClass === 'not-clicked' && likeClass === 'liked'){
          $(`.dislike-btn${post_id}`).children()[0].classList.remove('not-clicked');
          $(`.dislike-btn${post_id}`).children()[0].classList.add('disliked');
          $(`.like-btn${post_id}`).children()[0].classList.remove('liked');
          $(`.like-btn${post_id}`).children()[0].classList.add('not-clicked');
          dislikeRes = dislikeTrimCount + 1;
          likeRes = trimCount - 1;

        } else if (dislikeClass === 'not-clicked'){
          $(`.dislike-btn${post_id}`).children()[0].classList.remove('not-clicked');
          $(`.dislike-btn${post_id}`).children()[0].classList.add('disliked');
          dislikeRes = dislikeTrimCount + 1;
        } else {
          $(`.dislike-btn${post_id}`).children()[0].classList.remove('disliked');
          $(`.dislike-btn${post_id}`).children()[0].classList.add('not-clicked');
          dislikeRes = dislikeTrimCount - 1;
          
        }
        const dislikes = $(`.dislike-count${post_id}`).text(dislikeRes);

        const likes = $(`.like-count${post_id}`).text(likeRes);
      },
      error: function(response){
        console.log('error', response)
      }
    })
  });
