# 練習問題7.4

簡単なNewReaderを実装し、HTMLパーサが文字列から入力を受け取るようにしよう

## 内容

ちょっと今回は丁寧め
標準入力から直接渡されているこの形を変更する  

~~~
doc, err := html.Parse(os.Stdin)
~~~

`html.Parse`を調べてみると、`io.Reader`が欲しいらしい



~~~
$ go doc golang.org/x/net/html.Parse
func Parse(r io.Reader) (*Node, error)
    Parse returns the parse tree for the HTML from the given Reader. The input
    is assumed to be UTF-8 encoded.
~~~

じゃあ、`os.Stdin`も`io.Reader`なんだね！！


(ところどころ省略）
~~~
$ go doc os.Stdin
var (
        Stdin  = NewFile(uintptr(syscall.Stdin), "/dev/stdin")
        Stdout = NewFile(uintptr(syscall.Stdout), "/dev/stdout")
        Stderr = NewFile(uintptr(syscall.Stderr), "/dev/stderr")
)

$ go doc os.NewFile
func NewFile(fd uintptr, name string) *File

$ go doc os.File
type File struct {
        // Has unexported fields.
}
    File represents an open file descriptor.


func Create(name string) (*File, error)
func NewFile(fd uintptr, name string) *File
func Open(name string) (*File, error)
func OpenFile(name string, flag int, perm FileMode) (*File, error)
func Pipe() (r *File, w *File, err error)
func (f *File) Chdir() error
func (f *File) Chmod(mode FileMode) error
func (f *File) Chown(uid, gid int) error
func (f *File) Close() error
func (f *File) Fd() uintptr
func (f *File) Name() string
func (f *File) Read(b []byte) (n int, err error)
func (f *File) ReadAt(b []byte, off int64) (n int, err error)
func (f *File) Readdir(n int) ([]FileInfo, error)
func (f *File) Readdirnames(n int) (names []string, err error)
func (f *File) Seek(offset int64, whence int) (ret int64, err error)
func (f *File) Stat() (FileInfo, error)
func (f *File) Sync() error
func (f *File) Truncate(size int64) error
func (f *File) Write(b []byte) (n int, err error)
func (f *File) WriteAt(b []byte, off int64) (n int, err error)
func (f *File) WriteString(s string) (n int, err error)

$ go doc io.Reader
type Reader interface {
        Read(p []byte) (n int, err error)
}
~~~

方針としては、文字列を渡すと`io.Reader`を返す処理をかけばよい  
まずは、7.2で学習したとおり構造体を定義して、さらに`Read`メソッドを定義して`io.Reader`型にする  

NewReader関数は文字列を渡して、この`io.Reader`型を返すことができればクリア

~~~
$ go run main.go
<html>
  <head>
    <title> Title </title>
  </head>
  <body>
  Body
  </body>
</html>
&{<nil> 0xc4200500e0 0xc4200500e0 <nil> <nil> 2    []}
~~~

`html.Parse()`でエラーが検知されていないため、入力を受け取ることができたと考えられる

## 疑問点

自分の中で腑に落ちない点があったのでメモ  

~~~
func NewReader(s string) *Reader { return &Reader{s, 0, -1} }
~~~

参考にした`strings.NewReader()`である  
Reader型の構造体にs,0,-1をセットしてアドレスを返していると思われるが、Reader型にはフィールドがない  

動作するために`s string`フィールドを定義したが、なぜこれで動いているのか理解できなかった  

ただ、構造体とかの勉強は飛ばしてしまったので、普通の基礎知識を持っていないだけかもしれない