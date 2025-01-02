const InfoPopup = ({ infoText }) => {
    return (
      <span className="relative group">
        <span className="inline-block w-4 h-4 bg-gray-300 text-center text-xs font-bold rounded-full cursor-pointer">
          i
        </span>
        <span className="absolute left-0 -top-6 opacity-0 group-hover:opacity-100 transition bg-gray-700 text-white text-xs rounded p-1 z-10">
          {infoText}
        </span>
      </span>
    );
  };
  
  export default InfoPopup;
  