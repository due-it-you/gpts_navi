function Header() {
    return (
        <div className="bg-white border-b border-gray-400 p-4">
            <div className="flex justify-between items-center">
                <button className="bg-gray-200 hover:bg-gray-300 text-black font-bold py-2 px-4 rounded">
                    新規登録する
                </button>
                <button className="bg-gray-200 hover:bg-gray-300 text-black font-bold py-2 px-4 rounded">
                    ログインする
                </button>
            </div>
        </div>
    );
}

export default Header;