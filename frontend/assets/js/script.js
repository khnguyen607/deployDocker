function setCookie(name, value, daysToExpire) {
    var expirationDate = new Date();
    expirationDate.setDate(expirationDate.getDate() + daysToExpire);

    var cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expirationDate.toUTCString() + '; path=/';

    document.cookie = cookie;
}
fetch('server.txt')
    .then(response => response.text())
    .then(server => {

        function check() {
            function getCookie(cname) {
                let name = cname + "=";
                let decodedCookie = decodeURIComponent(document.cookie);
                let ca = decodedCookie.split(';');
                for (let i = 0; i < ca.length; i++) {
                    let c = ca[i];
                    while (c.charAt(0) == ' ') {
                        c = c.substring(1);
                    }
                    if (c.indexOf(name) == 0) {
                        return c.substring(name.length, c.length);
                    }
                }
                return "";
            }

            const formData = {
                user: getCookie('user'),
                password: getCookie('password'),
            };
            fetch(server + '/checked', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
                .then(response => response.text())
                .then(data => {
                    if (data == 1) {

                    } else {
                        window.location.href = 'login.html?error'
                    }
                })
        }
        check()

        fetch(server + '/getads')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                document.querySelector('footer div').innerHTML = data
            })
        document.querySelectorAll('.copy_data').forEach(copy => {
            copy.addEventListener('click', () => {
                var clipboard = ''
                var count = 1
                document.querySelectorAll('.data_ks:checked').forEach(item => {
                    item = item.parentNode.parentNode
                    var td = Array.from(item.querySelectorAll('td')).filter(div => !div.classList.contains('d-none'));
                    clipboard += count + '. ' + td[0].textContent + '\n'
                    // clipboard += count+'.'+td[0].textContent+'\n'+td[1].querySelector('strong').textContent
                    for (let i = 1; i < td.length; i++) {
                        clipboard += `${td[i].querySelector('.mt-1').innerHTML.replace(/<br>|Giá:/g, function (match) {
                            return match === '<br>' ? "--" : '';
                        }).replace(/\n+/g, '').replace(/\s/g, '').replace(/--/g, '; ')}\n`
                    }
                    clipboard += '\n'
                    count++
                })

                // Tạo một textarea ẩn để chứa nội dung cần copy
                var tempInput = document.createElement("textarea");
                tempInput.value = clipboard;
                // Thêm textarea vào DOM
                document.body.appendChild(tempInput);
                // Chọn toàn bộ nội dung trong textarea
                tempInput.select();
                tempInput.setSelectionRange(0, 99999);
                // Thử copy vào clipboard
                document.execCommand("copy");
                // Loại bỏ textarea khỏi DOM
                document.body.removeChild(tempInput);
                // Thông báo hoặc thực hiện các bước khác nếu cần thiết
                // alert("Đã copy vào clipboard: ");

                var btn = copy.parentNode
                btn.querySelector('span').classList.remove('d-none')
                btn.querySelector('span').textContent = 'Copy thành công';
                // Thêm đoạn HTML vào div sau 1 giây
                setTimeout(() => {
                    btn.querySelector('span').classList.add('d-none');
                }, 2000);
            })
        })

        $(function () {
            var availableTags = [
                "Vinpearl Beachfront Nha Trang",
                "Vinpearl Resort & Golf Nam Hội An",
                "Vinpearl Wonderworld Phú Quốc",
                "Vinpearl Sealink Nha Trang",
                "Vinpearl Resort & Spa Phú Quốc",
                "Vinpearl Resort & Spa Nha Trang Bay",
                "Vinpearl Resort Nha Trang",
                "Vinpearl Luxury Nha Trang",
                "Vinpearl Resort & Spa Hội An",
                "Vinpearl Resort & Spa Đà Nẵng",
                "Vinpearl Golflink Nha Trang",
                "VinHolidays Fiesta Phú Quốc",
                "Vinpearl Resort & Spa Hạ Long",
                "Hòn Tằm Resort"
            ];
            $("#ks").autocomplete({
                source: availableTags
            });
        });

        $(function () {
            $('input[name="daterange"]').daterangepicker({
                opens: 'left'
            }, function (start, end, label) {
                console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
            });
        });
        var table = document.querySelector('.data__list').cloneNode(true)
        var data_t = document.querySelector('.data_t').cloneNode(true)
        function confDefault() {
            document.querySelector('.data__list').innerHTML = table.innerHTML
            document.querySelector('.data_t').innerHTML = data_t.innerHTML
            document.querySelector('.data__list').innerHTML = ''
            document.querySelector('#pickalls').addEventListener('click', () => {
                document.querySelectorAll('.data_ks').forEach(item => {
                    document.querySelector('#pickalls').checked == true ? item.checked = true : item.checked = false
                })
            })
        }
        document.getElementById('myForm').addEventListener('submit', async (event) => {
            document.querySelector('.table__data').classList.add('d-none')
            document.querySelector('#myForm button').disabled = true
            // cấu hình mặc định
            confDefault()

            var status = document.querySelector('.table__status')
            status.innerHTML = '<h3 class="text-center">Đang tìm kiếm thông tin...</h3>'
            event.preventDefault();

            const formData = {
                ks: document.getElementById('ks').value,
                date: date.value.split(' - ').map(part => {
                    const [day, month, year] = part.split('/');
                    return `${year}-${month}-${day}`;
                }).join(' - ')
            }

            // fetch(server + '/submit', {
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: JSON.stringify(formData)
            // })
            //     .then(response => response.json())
            //     .then(data => {
            //         document.querySelector('#myForm button').disabled = false
            //         console.log(data)
            //         if (data == -1) {
            //             status.innerHTML = '<h2 class="text-center">Không có dữ liệu</h2>'
            //         } else if (data == false) {
            //             status.innerHTML = '<h3 class="text-center">Vui lòng thử lại..</h3>'
            //         } else {
            //             room = Object.keys(data)
            //             room.sort((a, b) => {
            //                 return Object.keys(data[b]).length - Object.keys(data[a]).length
            //             })
            //             groupPack = Object.keys(data[room[0]])

            //             console.log(groupPack);
            //             // in ra nội dung cột 
            //             groupPack.forEach(item => {
            //                 let th = document.createElement('th')
            //                 th.textContent = item
            //                 th.setAttribute('scope', 'col')
            //                 document.querySelector('.data_t').appendChild(th)
            //             })

            //             // in nội dung từng dòng
            //             room.forEach(ro => {
            //                 let tr = table.querySelector('.data__detail').cloneNode(true)
            //                 // document.querySelector('.data__list').innerHTML = ''
            //                 tr.querySelectorAll('td')[0].textContent = ro
            //                 groupPack.forEach(pa => {
            //                     let td = document.createElement('td')
            //                     td.classList.add('col-md')
            //                     if (data[ro][pa]) {
            //                         var pack = Object.keys(data[ro][pa])[0]
            //                         let foundSubstring = pa.split('/').find(substring => pack.includes(substring))
            //                         let price = foundSubstring + ':' + data[ro][pa][pack]['Price'].toLocaleString() + 'K'
            //                         if (data[ro][pa][pack]['adult'] > 0) price += ('<br>NL:' + data[ro][pa][pack]['adult'].toLocaleString() + 'K')
            //                         if (data[ro][pa][pack]['child'] > 0) price += ('<br>TE:' + data[ro][pa][pack]['child'].toLocaleString() + 'K')
            //                         td.innerHTML = `
            //                             <strong style="font-size: 0.8em;">
            //                                 ${pack}
            //                             </strong>
            //                             <div class="mt-1">
            //                                 ${price}
            //                             </div>
            //                         `
            //                         tr.appendChild(td)
            //                     } else {
            //                         td.innerHTML = `
            //                         <strong style="font-size: 0.8em;" class="text-danger"">
            //                             HẾT PHÒNG
            //                         </strong>
            //                     `
            //                         tr.appendChild(td)
            //                     }
            //                 })
            //                 document.querySelector('.data__list').appendChild(tr)
            //             })
            //             document.querySelector('.table__data').classList.remove('d-none')
            //             status.innerHTML = ''
            //         }
            //     })
            //     .catch((error) => {
            //         status.innerHTML = '<h3 class="text-center">Lỗi khi tìm kiếm</h3>' + error
            //         document.querySelector('#myForm button').disabled = false
            //     })

            async function fetchData(endP) {
                try {
                    const response = await fetch(server + endP, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(formData)
                    });
                    const data = await response.json();
                    confDefault()
                    // Sử dụng dữ liệu ở đây
                    console.log(data);
                    if (data) {
                        document.querySelector('#myForm button').disabled = false
                        console.log(data)
                        if (data == -1) {
                            status.innerHTML = '<h2 class="text-center">Không có dữ liệu</h2>'
                        } else if (data == false) {
                            status.innerHTML = '<h3 class="text-center">Vui lòng thử lại..</h3>'
                        } else {
                            room = Object.keys(data)
                            room.sort((a, b) => {
                                return Object.keys(data[b]).length - Object.keys(data[a]).length
                            })
                            groupPack = Object.keys(data[room[0]])

                            console.log(groupPack);
                            // in ra nội dung cột 
                            groupPack.forEach(item => {
                                let th = document.createElement('th')
                                th.textContent = item
                                th.setAttribute('scope', 'col')
                                document.querySelector('.data_t').appendChild(th)
                            })

                            // in nội dung từng dòng
                            room.forEach(ro => {
                                let tr = table.querySelector('.data__detail').cloneNode(true)
                                // document.querySelector('.data__list').innerHTML = ''
                                tr.querySelectorAll('td')[0].textContent = ro
                                groupPack.forEach(pa => {
                                    let td = document.createElement('td')
                                    td.classList.add('col-md')
                                    if (data[ro][pa]) {
                                        var pack = Object.keys(data[ro][pa])[0]
                                        let foundSubstring = pa.split('/').find(substring => pack.includes(substring))
                                        let price = foundSubstring + ':' + data[ro][pa][pack]['Price'].toLocaleString() + 'K'
                                        if (data[ro][pa][pack]['adult'] > 0) price += ('<br>NL:' + data[ro][pa][pack]['adult'].toLocaleString() + 'K')
                                        if (data[ro][pa][pack]['child'] > 0) price += ('<br>TE:' + data[ro][pa][pack]['child'].toLocaleString() + 'K')
                                        td.innerHTML = `
                                            <strong style="font-size: 0.8em;">
                                                ${pack}
                                            </strong>
                                            <div class="mt-1">
                                                ${price}
                                            </div>
                                        `
                                        tr.appendChild(td)
                                    } else {
                                        td.innerHTML = `
                                        <strong style="font-size: 0.8em;" class="text-danger"">
                                            HẾT PHÒNG
                                        </strong>
                                    `
                                        tr.appendChild(td)
                                    }
                                })
                                document.querySelector('.data__list').appendChild(tr)
                            })
                            document.querySelector('.table__data').classList.remove('d-none')
                            status.innerHTML = ''
                        }
                    }
                } catch (error) {
                    console.error('Đã xảy ra lỗi:', error);
                }
            }

            fetchData('/submitF');
            fetchData('/submit');

        })
    })
