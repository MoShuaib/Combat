let nextBtn = document.getElementById("next_btn");
        let changePage = document.getElementById("changePage");
        nextBtn.addEventListener("click", ()=>{
            let list1 = document.getElementById("list");
            values = list1.value;
            if (values == "fighter") {
                changePage.href = "fighter.html"
            }
            else {
                changePage.href = "register.html"
            }
        })

