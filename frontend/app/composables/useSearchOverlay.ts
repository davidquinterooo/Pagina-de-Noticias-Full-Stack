export const useSearchOverlay = () => {
  const isOpen = useState('search-overlay-open', () => false)

  const open = () => { isOpen.value = true }
  const close = () => { isOpen.value = false }

  return { isOpen, open, close }
}