import axios from 'axios';
import React, { useState } from 'react'


const Hero = () => {
  const [input, setInput] = useState("");
  const [result, setResult] = useState(false);

  const checkInputAPI = () => {
    axios.postForm("https://finalproject-tbo-production.up.railway.app/api/check", {
      query:input
    }, {
      headers:{
        'Content-Type': 'application/json'
      },
      withCredentials:false
    }).then((res) => {
      setResult(res.data.result)
    })
  }

  const onChangeInput = (data) => {
    setInput(data.target.value);
    if (data.target.value) {
      alert(`Kalimat ${input} adalah kalimat baku`)
    }else{
      alert(`Kalimat ${input} adalah kalimat tidak baku`)
    }
  }

  return (
    <>
      <div className="w-full h-[80vh]">
        <div className="pt-12 mx-auto text-center justify-center items-center">
          <h1 className="font-abc text-whitening text-3xl font-semibold">Parsing Kalimat</h1>
        </div>
        
        <div className="mt-10 text-[Poppins] md:ml-64 md:mr-64 ml-10 mr-10">
          <p className="text-graying text-lg font-medium pb-2">Kalimat Bahasa Indonesia</p>
          
          <form>
            <input value={input} onChange={onChangeInput} type="text" placeholder="Input String Disini" className="text-gray-800 border-2 border-graying px-3 py-3 font-light rounded-lg text-md w-full"/>
            <div className="flex pt-4 items-center justify-center">
              <button onClick={checkInputAPI} type="button" className="text-white bg-graying px-6 py-3 rounded-lg font-medium">Parsing</button>
            </div>
          </form>
          <p className="text-graying text-lg font-medium mt-12">Hasil Pengecekan</p>
        </div>
      </div>

    </>
  )
}

export default Hero