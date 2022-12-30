import axios from 'axios';
import React, { useState } from 'react'


const Hero = () => {
  const [input, setInput] = useState("");
  const [result, setResult] = useState(false);
  const [fetch, setFetch] = useState(false);
  const [tempString, setTempString] = useState("");

  const checkInputAPI = () => {
    if (input.length === 0) {
      return alert("Masukan input string terlebih dahulu")
    }
    axios.postForm("https://finalproject-tbo-production.up.railway.app/api/check", {
      query:input
    }).then((res) => {
      setTempString(input)
      setResult(res.data.result)
      setFetch(true);
    })
  }

  const onChangeInput = (data) => {
    setInput(data.target.value);
  }

  return (
    <>
      <div className="w-full pb-20">
        <div className="pt-12 mx-auto text-center justify-center items-center">
          <h1 className="font-abc text-whitening text-3xl font-semibold">Parsing Kalimat</h1>
        </div>
        
        <div className="mt-10 text-[Poppins] md:ml-64 md:mr-64 ml-10 mr-10">
          <p className="text-graying text-lg font-medium pb-2">Kalimat Bahasa Indonesia</p>
          <form className="flex">
            <input value={input} onChange={onChangeInput} type="text" placeholder="Input String Disini" className="text-gray-800 border-2 border-graying px-3 py-3 font-light text-md w-full"/>
            <div className="flex items-center justify-center">
              <button onClick={checkInputAPI} type="button" className="text-white h-full bg-green-700 px-6 py-3 font-medium">Parsing</button>
            </div>
          </form>

          {
            fetch && <p className="text-graying text-lg font-medium mt-12">Hasil Pengecekan</p>
          }
      
          {(fetch && result) &&
          <div class="bg-teal-100 border-t-4 border-teal-500 rounded-b text-teal-900 px-4 py-3 shadow-md mt-5" role="alert">
            <div class="flex">
              <div class="py-1"><svg class="fill-current h-6 w-6 text-teal-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z"/></svg></div>
              <div>
                <p class="font-bold">Kalimat "{tempString}" adalah kalimat baku</p>
              </div>
            </div>
          </div>
          }

          {(fetch && !result) &&
          <div class="bg-red-100 border-t-4 border-red-500 rounded-b text-red-900 px-4 py-3 shadow-md mt-5" role="alert">
          <div class="flex">
            <div class="py-1"><svg class="fill-current h-6 w-6 text-red-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z"/></svg></div>
            <div>
              <p class="font-bold">Kalimat "{tempString}" adalah kalimat tidak baku</p>
            </div>
          </div>
        </div>
          }
        </div>
      </div>

    </>
  )
}

export default Hero