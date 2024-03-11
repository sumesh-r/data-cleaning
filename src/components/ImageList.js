export default function ImageList({ images }) {
  return (
    <div className="flex flex-col items-center">
      {images.map((image, index) => (
        <div key={index} className="w-1/2 p-2">
          <img
            src={`/${image}`}
            alt={`Image ${index + 1}`}
            className="w-full h-auto"
          />
        </div>
      ))}
    </div>
  );
}
