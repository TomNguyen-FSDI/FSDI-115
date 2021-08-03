
$('.like-container').submit(function(e){
    e.preventDefault();
    const post_id = $(this).attr('id');
    const url = $(this).attr('action');
    // likes front end vars and consts
    const likeClass = $(`.like-btn${post_id}`).children()[0].classList[2];
    
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
        if(likeClass === 'not-clicked' && dislikeClass === 'disliked'){
          $(`.like-btn${post_id}`).children()[0].classList.remove('not-clicked');
          $(`.like-btn${post_id}`).children()[0].classList.add('liked');
          $(`.dislike-btn${post_id}`).children()[0].classList.remove('disliked');
          $(`.dislike-btn${post_id}`).children()[0].classList.add('not-clicked');
          likeRes = trimCount + 1;
          dislikeRes = dislikeTrimCount - 1;

        } else if(likeClass === 'not-clicked'){
          $(`.like-btn${post_id}`).children()[0].classList.remove('not-clicked');
          $(`.like-btn${post_id}`).children()[0].classList.add('liked');
          likeRes = trimCount + 1;
        }else {
          $(`.like-btn${post_id}`).children()[0].classList.remove('liked');
          $(`.like-btn${post_id}`).children()[0].classList.add('not-clicked');

          likeRes = trimCount - 1;
        }
        const likes = $(`.like-count${post_id}`).text(likeRes);

        const dislikes = $(`.dislike-count${post_id}`).text(dislikeRes);
      },
      error: function(response){
        console.log('error', response);
      }
    })
  });