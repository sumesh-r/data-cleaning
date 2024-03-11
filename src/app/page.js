"use client";
import ImageList from "@/components/ImageList";
import { useState } from "react";
export default function Home() {
  const [file, setFile] = useState("");
  const [bimages, setBImages] = useState([]);
  const [aimages, setAImages] = useState([]);
  const onSubmit = async (e) => {
    e.preventDefault();
    const bresponse = await fetch(`http://localhost:5000/images`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        file: file,
      }),
    });
    const bdata = await bresponse.json();
    setBImages(Object.values(bdata)[0]);

    const aresponse = await fetch(`http://localhost:5000/aimages`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        file: file,
      }),
    });
    const adata = await aresponse.json();
    setAImages(Object.values(adata)[0]);
  };
  return (
    <div className="bg-white">
      {/* header */}
      <div className="flex w-full justify-between px-10 py-5">
        <div className="text-2xl font-semibold">Data Cleaner</div>
      </div>
      <div className="w-full border-b border-gray-400"></div>
      {/* get file */}
      <form
        onSubmit={onSubmit}
        className="flex w-full pt-10 flex-col items-center  justify-center"
      >
        <div className="font-bold py-5 text-3xl">Clean Data</div>
        <div>Upload your dataset to start the cleaning process.</div>
        <div>
          <label
            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            htmlFor="file_input"
          >
            Upload file
          </label>
          <input
            className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50"
            id="file_input"
            // value={file}
            onChange={(e) => {
              setFile(
                `${process.env.NEXT_PUBLIC_DIR}${e.target.files[0].name}`
              );
            }}
            type="file"
          />
        </div>
        <button
          type="submit"
          className="px-3 py-2 bg-blue-600 text-white rounded-lg mt-5"
        >
          SUBMIT
        </button>
      </form>
      {/* show images */}
      {bimages && (
        <div className="flex w-full justify-center mt-5 mb-10">
          <div className="space-y-3">
            <div className="text-center text-xl font-semibold">
              Before Cleaning
            </div>
            <ImageList images={bimages} />
          </div>
          <div className="space-y-3">
            <div className="text-center text-xl font-semibold">
              After Cleaning
            </div>
            <ImageList images={aimages} />
          </div>
        </div>
      )}
    </div>
  );
}
