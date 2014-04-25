pkgname=b-icons-git
_pkgname=b-icons
pkgver=2.0.0
pkgrel=1
pkgdesc="B-icons is a stylized Tango-esque Linux desktop icon set. They are designed to be a clear, simple and consistent."
arch=('any')
url="https://github.com/burhanilinux/b-icons.git
license=('GPL3')
depends=()
makedepends=('git')
optdepends=()
provides=('b-icons-git')
conflicts=('b-icons-git')
source=('git+https://github.com/burhanilinux/b-icons.git')
md5sums=('SKIP')

pkgver() {
  cd $srcdir/$_pkgname
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {

  # create theme dirs
  install -d -m 755 "$pkgdir"/usr/share/icons/B-icons

  # install theme
  cd $srcdir/moka-icon-theme/B-icons
  cp -r . "$pkgdir"/usr/share/icons/B-icons/
}
